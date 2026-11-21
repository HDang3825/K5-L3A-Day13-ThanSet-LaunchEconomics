# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.805 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | Tổng các khoản trên | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (Token + Tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Chi phí mỗi việc thành công (4.472 đ [simulated]) gấp **16,3 lần** so với hoá đơn token + tool chia đều cho 1.200 yêu cầu (274,7 đ).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Khoản lớn nhất là **làm lại chiếm 51,8%** (2.264.000 đ [simulated]), tiếp theo là xem lại chiếm 40,7% (1.780.000 đ [simulated]); tổng giờ nhân viên chiếm tới 92,5% [simulated] chi phí.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× [simulated] |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× [simulated] |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× [simulated] |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× [simulated] |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? Loại **quoc_te** không đáng xử lý vì chi phí lên tới 22.515 đ (1,88× nhân viên tự làm, tỉ lệ thành công chỉ 27,3%). Cho chạy lại không giúp vì tỉ lệ thành công giảm mạnh theo từng lần chạy (lần 1: 30%, lần 2: 11,4%, lần 3: 2,2%), chỉ làm tăng chi phí vô ích.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× [simulated] |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Chi phí cố định (40 triệu đ/tháng) không làm thay đổi kết luận vì ở cả quy mô đầy đủ (4.599 đ = 0,38×) lẫn khi giảm một nửa khối lượng (5.784 đ = 0,48× [simulated]), chi phí đều thấp hơn đáng kể so với mức cơ sở 12.000 đ của nhân viên tự làm.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: Chi phí mỗi việc thành công vọt lên **6.543 đ (+46,3%)** [simulated], bằng đúng tổng hai mức tăng riêng rẽ (+5,6% và +40,7%) do mô hình chi phí có tính chất cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại (+51,8%)** · 2. **Tỉ lệ xem lại (+40,7%)** · 3. **Lương nhân viên (+23,1%)**. Biến động giá token ảnh hưởng ít nhất (chỉ $\pm 5,6\%$).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [sim] | 319 | 7.449.781 đ [sim] | 4.111 đ [simulated] |
| 2 lần | 4.093.220 đ [sim] | 234 | 6.901.220 đ [sim] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [sim] | 222 | 7.037.585 đ [sim] | 4.472 đ [simulated] |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn **2 lần chạy là rẻ nhất cho công ty (6.901.220 đ [simulated])**. Con số này **không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần: 4.111 đ), vì nếu chỉ chạy 1 lần sẽ đẩy thêm 85 yêu cầu sang nhân viên xử lý với mức phí 12.000 đ/yêu cầu.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Đạt **11.743 đ (0,98×)** [simulated] nếu làm lại mất 9 phút/ca, và tăng lên **12.414 đ – 12.516 đ (1,03× – 1,04×)** [simulated] nếu tính theo số phút làm lại thực tế, tức đắt hơn cả nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? Pilot phải đo lường để tìm ra tỉ lệ xem lại an toàn thấp nhất có thể (thay vì 100%) và kiểm soát thời gian xem lại của mỗi ca không vượt quá ngưỡng hòa vốn là **4,8 – 5,1 phút**, nhằm bảo toàn giá trị kinh tế của trợ lý AI.
