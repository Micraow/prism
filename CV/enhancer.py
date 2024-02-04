import cv2
import numpy as np
import cv2


def order_points(points):
    """
    坐标点排序
    :param points: 轮廓坐标
    :return: 返回排序完的坐标
    """

    # 一共4个坐标点， 左上, 右上, 右下, 左下
    rect = np.zeros((4, 2), dtype=np.float32)

    # 计算左上, 右下
    s = points.sum(axis=1)
    rect[0] = points[np.argmin(s)]  # 和最小的是左上
    rect[2] = points[np.argmax(s)]  # 和最大的是右下

    # 计算右上, 左下
    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]  # 差最小的是右上
    rect[3] = points[np.argmax(diff)]  # 差最小的是左下

    # 返回
    return rect


def four_point_transform(image, pts):
    """
    透视变换 (拉伸为长方形)
    :param image: 原始图像
    :param pts: 坐标点
    :return: 透视变换后的图
    """

    # 获取输入坐标点
    rect = order_points(pts)
    (top_left, top_right, bottom_left, bottom_right) = rect

    # 计算最大的w (勾股定理w = (Δx^2 + Δy^2)^1/2)
    widthA = np.sqrt(((bottom_right[0] - bottom_left[0])
                     ** 2) + ((bottom_right[1] - bottom_left[1]) ** 2))
    widthB = np.sqrt(((top_right[0] - top_left[0])
                     ** 2) + ((top_right[1] - top_left[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # 计算最大的y (勾股定理y = (Δx^2 + Δy^2)^1/2)
    heightA = np.sqrt(((top_right[0] - bottom_right[0])
                      ** 2) + ((top_right[1] - bottom_right[1]) ** 2))
    heightB = np.sqrt(
        ((top_left[0] - bottom_left[0]) ** 2) + ((top_right[1] - top_left[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # 变换后对应坐标位置
    dst = np.array(
        [[0, 0],
         [maxWidth - 1, 0],
         [maxWidth - 1, maxHeight - 1],
         [0, maxHeight - 1]],
        dtype=np.float32
    )

    # 计算变换矩阵
    M = cv2.getPerspectiveTransform(rect, dst)
    print("变换矩阵:\n", M)  # 调试输出

    # 透视变换
    wraped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # 返回
    return wraped


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    修改图片大小
    :param image: 原图
    :param width: 宽
    :param height: 高
    :param inter: 模式
    :return: 修改好的图片
    """

    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)

    # 返回
    return resized


def read_image(image_path):
    """
    读取图片
    :param image_path: 图片路径
    :return: 返回原始图片, 裁剪后的图片, 边缘, 图片伸缩比例
    """

    # 读取图片
    image = cv2.imread(image_path)

    # 计算伸缩比例
    ratio = image.shape[0] / 500.0

    # 深拷贝
    image_copy = image.copy()

    # 缩放大小
    image_resize = resize(image_copy, height=500)

    # 转换成灰度图
    image_gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)

    # 高斯滤波
    image_gaussian = cv2.GaussianBlur(image_gray, (5, 5), 0)

    # Canny边缘检测
    edge = cv2.Canny(image_gaussian, 75, 200)

    # 返回
    return image, image_resize, edge, ratio


def image_calculate_contours(image_resize, edge):
    """
    计算轮廓
    :param image_resize: 裁剪后的图片
    :param edge: 边缘
    :return: 外接长方形数组
    """

    # 轮廓检测
    contours, hierarchy = cv2.findContours(
        edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 轮廓排序
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # 取最大的5个
    contours_5 = contours[:5]

    # 长方形数字
    approx_array = []

    # 遍历轮廓
    for c in contours_5:

        # 计算轮廓周长
        length = cv2.arcLength(c, True)

        # 计算大约轮廓
        approx = cv2.approxPolyDP(c, 0.02 * length, True)

        # 如果是四边形, 取出
        if len(approx) == 4:
            approx_array.append(approx)

    return approx_array

def image_transform(image, approx_array, ratio):
    """
    图片转换
    :param image: 原始图像
    :param approx_array: 外接长方形坐标数组
    :param ratio: 图片拉伸比例
    :return: 返回最终结果
    """

    # 透视变换
    warped = four_point_transform(image, approx_array[0].reshape(4, 2) * ratio)

    # 转换为灰度图
    warped_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

    # # 二值化
    # ret, thresh = cv2.threshold(warped_gray, 190, 255, cv2.THRESH_BINARY)

    # 自适应阈值
    # thresh = cv2.adaptiveThreshold(warped_gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 4)

    thresh = cv2.adaptiveThreshold(warped_gray ,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 13)

    return thresh


def enhance(image_path):
    image, image_resize, edge, ratio = read_image(image_path=image_path)
    approx_array = image_calculate_contours(image_resize, edge)
    final_result = image_transform(
        image=image, approx_array=approx_array, ratio=ratio)
    return final_result