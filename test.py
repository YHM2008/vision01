# 本课第一个脚本：读取图片 -> 打印尺寸 -> 显示 -> 保存
import cv2

# 读取图片(img_path需要手动指定类似.../test.png,只写test.png默认在当前目录)
img_path= r"../images/photo.png"
img = cv2.imread(img_path)

# 先判断有没有读到，再往下用
if img is None:
    print("读取失败：图片路径不对，或者文件不存在")
else:
    # 打印图片尺寸：高度 宽度 通道数
    print("图片尺寸：", img.shape)

    # 在窗口里显示
    cv2.imshow("test", img)
    cv2.waitKey(0)          # 等待按任意键
    cv2.destroyAllWindows() # 关掉所有窗口

    # 保存到 out 目录(out_path需要手动指定类似.../test.png,只写test.png默认在当前目录)
    out_path=r"D:\vision01\out\result.jpg"
    cv2.imwrite(out_path, img)
