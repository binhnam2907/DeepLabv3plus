'''
Squeeze-and-Excitation (SE) là một phương pháp được đề xuất để tăng cường khả năng học và khả năng biểu diễn của các mô hình học sâu, đặc biệt là trong mạng nơ-ron tích chập (CNN).
Ý tưởng chính của SE là tập trung vào việc mô hình hóa sự phụ thuộc giữa các kênh (channel) của đặc trưng đầu vào và lượng thông tin quan trọng trong mỗi kênh đó. SE thực hiện điều này bằng cách sử dụng một cặp lớp "squeeze" và "excitation" để tạo ra một trọng số (weight) cho mỗi kênh.
Quá trình "squeeze" giảm chiều của đặc trưng đầu vào từ ba chiều (chiều cao, chiều rộng, số lượng kênh) xuống một chiều (số lượng kênh). Điều này thường được thực hiện bằng cách sử dụng lớp "Global Average Pooling" để tính giá trị trung bình của mỗi kênh, tạo thành một vector có kích thước bằng số lượng kênh.
Tiếp theo, quá trình "excitation" áp dụng một vài lớp mạng nơ-ron để học cách tạo ra một vector trọng số có kích thước bằng số lượng kênh ban đầu. Vector trọng số này được sử dụng để chỉ định độ quan trọng của mỗi kênh. Phần tử trong vector trọng số càng lớn, thì kênh tương ứng càng quan trọng.
Cuối cùng, các kênh trong đặc trưng đầu vào được điều chỉnh bằng cách nhân với tương ứng từng phần tử trong vector trọng số. Quá trình này giúp tăng cường thông tin quan trọng và làm yếu thông tin không quan trọng, từ đó cải thiện khả năng biểu diễn và khả năng học của mô hình.
SE đã được áp dụng thành công trong nhiều mô hình CNN tiên tiến và đã chứng minh sự cải thiện đáng kể về hiệu suất và độ chính xác trong các tác vụ như phân loại ảnh, phát hiện đối tượng và nhận dạng vị trí.
'''

'''
Accuracy: 0.97404
F1: 0.95379
Jaccard: 0.92124
Recall: 0.95885
Precision: 0.95683
'''