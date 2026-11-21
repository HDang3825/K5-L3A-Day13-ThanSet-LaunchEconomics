# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: ThanSet
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dựng hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN để trả lời bốn câu hỏi: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra được quyết định. Cách tiếp cận: tính chi phí thật từ trace (cả giờ nhân viên), tìm yếu tố nhạy nhất, phân loại lỗi theo nguyên nhân gốc, rồi thiết kế pilot có đối chứng, đủ cỡ mẫu và luật dừng viết trước. Mọi con số tính từ hai cột `_simulated` đều ghi nhãn `simulated`.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí mỗi việc thành công | Ba hàm A1 qua cả ba phép thử (1,20 · 1,25 · 1,25); hàm `mo_hinh` tính tử số trên mọi lần chạy, mẫu số chỉ đếm `thanh_cong`; tách theo 4 loại yêu cầu; cộng chi phí cố định 40 triệu đ/tháng | `src/lab13.py`, `bang_chi_phi.md` |
| B · Độ nhạy | 9 kịch bản đổi từng yếu tố, kịch bản cặp, giới hạn 1/2/3 lần chạy, xem lại 100% | `bang_chi_phi.md` |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, thống nhất ca lệch, bảng khắc phục 5 ca đủ 5 loại | `bang_loi.md` |
| D · Pilot | Chia ngẫu nhiên theo nhân viên, tính cỡ mẫu có hệ số thiết kế cụm (ICC 0,02), ba luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ | `pilot_plan.yaml` |
| E · Chỉ số, rủi ro, hồ sơ | Ba chỉ số tính thử, 8 event có `trace_id`, rủi ro kinh tế lấy số từ bảng độ nhạy, hồ sơ một trang bảy mục | `chi_so.md`, `ho_so_launch_v0.md` |

## 4. Kết quả

- **Chi phí mỗi việc thành công:** 4.472 đ (simulated), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí (simulated).
- **Theo loại yêu cầu (so với 12.000 đ nhân viên tự làm, simulated):** `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` 1,88×. `quoc_te` đắt hơn tự làm và chạy lại không giúp (tỉ lệ `ok` giảm từ 30,0% xuống 11,4% rồi 2,2% qua các lần thử). Cộng chi phí cố định: 4.599 đ (0,38×) ở 45.000 yêu cầu/tháng.
- **Ba yếu tố nhạy nhất (simulated):** số ca làm lại +51,8%, tỉ lệ xem lại +40,7%, lương nhân viên +23,1%; giá token chỉ +5,6%. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ) dù không cho chi phí mỗi việc thấp nhất (giới hạn 1 lần: 4.111 đ). Xem lại 100% làm chi phí lên 11.743–12.516 đ (0,98–1,04×), tức không tiết kiệm.
- **Chỉ số trong đợt chạy thử (không có đối chứng):** chỉ số chính 82,83% (994/1.200); tỉ lệ bỏ qua gợi ý 27,12% (48/177); lỗi lọt đến khách 4,25% (51/1.200).
- **Bảng lỗi:** đồng thuận 17/20 = 85%; ba ca lệch nhãn là 13, 16, 17, mỗi ca có một câu quy tắc phân biệt.
- **Pilot:** chia theo nhân viên, 20 người mỗi nhóm, 859 yêu cầu mỗi nhóm, hệ số thiết kế 6,96; chấp nhận mức chênh 6 điểm vì ở mức 5 điểm power chỉ còn 0,64. Phạm vi `noi_dia` + `hang_nang`; ngày quyết định 2026-12-19.
- **Đề xuất cuối: Go có điều kiện** cho kế hoạch pilot, với ba điều kiện: (1) Kỹ sư trưởng agent sửa khoá chống hoàn trùng và đối soát sổ cái (ca 7, 20) trước 2026-11-30; (2) Giám đốc vận hành ký chấp nhận mức chênh 6 điểm trước 2026-12-01; (3) PM trợ lý hoàn phí bật đủ event có `trace_id` và thay phút `_simulated` bằng phút đo thật sau tuần 1, trước 2026-12-08.
- **Kết quả duyệt chéo Gate 2a:** nhóm được chấm bởi nhóm: ... · điểm hội đồng cho nhóm: ... / 30 · quyết định của hội đồng: ... · câu hỏi và câu trả lời: ...

## 5. Khó khăn và cách xử lý

- **Gộp nhiều nhánh git:** mỗi thành viên làm trên một nhánh riêng nên `TEAM.md` và `ho_so_launch_v0.md` bị sửa cùng lúc và xung đột khi merge. Xử lý: gộp thủ công từng chỗ xung đột, giữ phần đầy đủ hơn, kiểm tra lại bằng `grep` sau khi gộp.
- **Trùng việc ở hồ sơ:** hồ sơ launch bị điền hai lần (bản của người giữ hồ sơ và bản của người viết code). Xử lý: giữ bản đầy đủ, người giữ hồ sơ chuyển sang rà soát và kiểm số (ví dụ tính tay 3.414 đ cho phạm vi `noi_dia` + `hang_nang`).
- **Nhãn lỗi lệch ở 3 ca (13, 16, 17):** do ranh giới giữa Hệ thống, Giới hạn hệ thống, Ngữ cảnh và Ngầm. Xử lý: thống nhất theo nguyên nhân gốc và ghi quy tắc phân biệt trong `bang_loi.md`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí giờ nhân viên (xem lại, làm lại) là số giả lập, chiếm 92,5% tổng chi phí: kết luận kinh tế phụ thuộc vào việc thay bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chỉ nói "chỉ số trong đợt chạy thử là …", không nói trợ lý đã nâng chỉ số.
- Chia theo nhân viên chỉ có 20 cụm mỗi nhóm (đạt ngưỡng tối thiểu) và phải chấp nhận mức chênh 6 điểm; còn rủi ro chia sẻ câu trả lời giữa các nhân viên cùng depot.
- Hướng cải thiện: đo phút thật bằng event `staff_review_decision` và `staff_rework_completed`, giảm xem lại theo bậc, thu hẹp thêm phạm vi nếu chi phí vượt 8.000 đ.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
- Đề bài và dữ liệu giả lập của lab: `docs/` và `src/` trong repo này
