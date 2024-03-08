import cv2
import numpy as np

def order_points(points):
    """
    对输入的点集进行排序，以便找到图像中的矩形边界。
    
    :param points: 输入的点集，通常是轮廓的顶点。
    :return: 排序后的点集，按照左上、右上、右下、左下的顺序。
    """
    # 初始化一个4x2的数组用于存放排序后的点
    rect = np.zeros((4, 2), dtype=np.float32)
    
    # 计算每个点的x和y坐标之和，找到左上和右下点
    s = points.sum(axis=1)
    rect[0] = points[np.argmin(s)]  # x和y坐标之和最小的点是左上
    rect[2] = points[np.argmax(s)]  # x和y坐标之和最大的点是右下
    
    # 计算每个点的x和y坐标之差，找到右上和左下点
    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]  # x坐标之差最小的点是右上
    rect[3] = points[np.argmax(diff)]  # x坐标之差最大的点是左下
    
    # 返回排序后的点集
    return rect

def four_point_transform(image, pts):
    """
    对图像进行透视变换，以便将图像中的不规则四边形区域转换为矩形。
    
    :param image: 待变换的原始图像。
    :param pts: 输入的四个点，通常是矩形的四个顶点。
    :return: 透视变换后的图像。
    """
    # 对输入的点进行排序
    rect = order_points(pts)
    
    # 计算矩形的宽度和高度
    widthA = np.sqrt((rect[1][0] - rect[0][0]) ** 2 + (rect[1][1] - rect[0][1]) ** 2)
    widthB = np.sqrt((rect[2][0] - rect[1][0]) ** 2 + (rect[2][1] - rect[1][1]) ** 2)
    maxWidth = max(int(widthA), int(widthB))
    
    heightA = np.sqrt((rect[2][0] - rect[3][0]) ** 2 + (rect[2][1] - rect[3][1]) ** 2)
    heightB = np.sqrt((rect[0][0] - rect[3][0]) ** 2 + (rect[0][1] - rect[3][1]) ** 2)
    maxHeight = max(int(heightA), int(heightB))
    
    # 定义目标点的坐标
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype=np.float32)
    
    # 计算透视变换矩阵
    M = cv2.getPerspectiveTransform(rect, dst)
    
    # 应用透视变换
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    # 返回变换后的图像
    return warped

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    调整图像大小。
    
    :param image: 原始图像。
    :param width: 新的宽度，如果None，则保持原始宽度。
    :param height: 新的高度，如果None，则保持原始高度。
    :param inter: 插值方法。
    :return: 调整大小后的图像。
    """
    # 获取原始图像的尺寸
    (h, w) = image.shape[:2]
    
    # 如果宽度和高度都未指定，则直接返回原始图像
    if width is None and height is None:
        return image
    
    # 计算新的尺寸
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    # 使用cv2.resize进行图像缩放
    resized = cv2.resize(image, dim, interpolation=inter)
    
    # 返回缩放后的图像
    return resized

def read_image(image_path):
    """
    读取图像并进行预处理。
    
    :param image_path: 图片路径。
    :return: 返回原始图片, 裁剪后的图片, 边缘, 图片伸缩比例。
    """
    # 读取图片
    image = cv2.imread(image_path)
    
    # 计算图片伸缩比例
    ratio = image.shape[0] / 500.0
    
    # 深拷贝原始图像
    image_copy = image.copy()
    
    # 缩放图像到指定高度
    image_resize = resize(image_copy, height=500)
    
    # 转换为灰度图
    image_gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
    
    # 应用高斯滤波
    image_gaussian = cv2.GaussianBlur(image_gray, (5, 5), 0)
    
    # 应用Canny边缘检测
    edge = cv2.Canny(image_gaussian, 75, 200)
    
    # 返回处理后的图像和边缘信息
    return image, image_resize, edge, ratio

def image_calculate_contours(image_resize, edge):
    """
    计算图像的轮廓。
    
    :param image_resize: 裁剪后的图片。
    :param edge: 边缘。
    :return: 外接长方形数组。
    """
    # 轮廓检测
    contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # 轮廓排序，按面积大小降序排列
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    # 取最大的5个轮廓
    contours_5 = contours[:5]
    
    # 初始化外接长方形数组
    approx_array = []
    
    # 遍历轮廓
    for c in contours_5:
        # 计算轮廓周长
        length = cv2.arcLength(c, True)
        
        # 计算轮廓的近似多边形
        approx = cv2.approxPolyDP(c, 0.02 * length, True)
        
        # 如果近似多边形是四边形，则添加到数组中
        if len(approx) == 4:
            approx_array.append(approx)
    
    # 返回外接长方形数组
    return approx_array

def image_transform(image, approx_array, ratio):
    """
    对图像进行透视变换和二值化处理。
    
    :param image: 原始图像。
    :param approx_array: 外接长方形坐标数组。
    :param ratio: 图片拉伸比例。
    :return: 返回最终结果。
    """
    # 对第一个外接长方形进行透视变换
    warped = four_point_transform(image, approx_array[0].reshape(4, 2) * ratio)
    
    # 转换为灰度图
    warped_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    
    # 应用自适应阈值进行二值化
    thresh = cv2.adaptiveThreshold(warped_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 13)
    
    # 返回二值化后的图像
    return thresh

def enhance(image_path):
    """
    增强图像，包括读取、轮廓计算、图像转换等步骤。
    
    :param image_path: 图片路径。
    :return: 返回增强后的图像。
    """
    # 读取并预处理图像
    image, image_resize, edge, ratio = read_image(image_path=image_path)
    
    # 计算轮廓
    approx_array = image_calculate_contours(image_resize, edge)
    
    # 对图像进行透视变换和二值化处理
    final_result = image_transform(image=image, approx_array=approx_array, ratio=ratio)
    
    # 返回增强后的图像
    return final_result
