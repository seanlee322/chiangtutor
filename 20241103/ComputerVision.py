import cv2

# 讀取此目錄中的(也就是路徑./)檔案lena.bmp，預設是RGB，因此一個像素有三個亮度值
lena1 = cv2.imread('lena.bmp')

# 和上面很像，但讀法由RGB改成灰階，因此一個像素只有一個亮度值
lena2 = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)

# 和上面很像，因為cv2中定義 cv2.IMREAD_GRAYSCALE 就等於 0，所以 lena3 和上面的 lena2 一模一樣
lena3 = cv2.imread('lena.bmp', 0)


# 顯示圖片
cv2.imshow('show lena1', lena1)
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()


# 印出lena1的維度資訊
print(lena1.shape)  

# 印出lena1的維度資訊，和上面一模一樣
import numpy as np
print(np.shape(lena1))  


# 取得lena1的高度和寬度(順序與平常的寬x高的說法相反)
height = lena1.shape[0]  # height是高度
width = lena1.shape[1]  # width是寬度


cv2.imwrite('lena1_output_j.jpg',lena1)  # 輸出成jpg檔
cv2.imwrite('lena1_output_p.png',lena1)  # 輸出成png檔
cv2.imwrite('lena1_output_b.bmp',lena1)  # 輸出成bmp檔
