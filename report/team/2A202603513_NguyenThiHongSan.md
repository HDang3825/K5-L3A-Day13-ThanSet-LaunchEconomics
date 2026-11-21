# Báo cáo cá nhân — Nguyễn Thị Hồng San - 2A202603513

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thị Hồng San
- MSSV: 2A202603513
- Email: 26ai.sannth@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ (Quản lý Hồ sơ & Vận hành, thành viên 4)

## 2. Phần việc phụ trách

- Giữ `report/team/ho_so_launch_v0.md` từ 14:00, gom số liệu từ thành viên 1, 2, 3 và điền dần qua từng checkpoint.
- Rà tính nhất quán: không có từ cấm theo quy tắc 5 của README, mọi số giả lập có nhãn `simulated`, người phụ trách là một chức danh cụ thể.
- CP3: gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 2); viết bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Gate 2a: gửi hồ sơ lúc 17:00; chấm nhóm bạn bằng `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- Điền thông tin nhóm, 4 thành viên và vai trong `TEAM.md`; dựng khung `ho_so_launch_v0.md` (nhóm, lớp, cột trạng thái, người phụ trách là chức danh cụ thể).
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (bộ nhãn người 2 trong `bang_loi.md`); đồng thuận với người gắn nhãn 1 là 17/20 = 85%.
- Rà soát hồ sơ launch v0 (bản hoàn chỉnh do TV1 điền) với vai trò người giữ hồ sơ: đối chiếu số với `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`; kiểm tra nhãn `simulated`, chức danh người phụ trách, từ cấm và chỗ còn trống.
- Tính tay kiểm số 3.414 đ ở mục 1 (chi phí mỗi việc thành công, phạm vi noi_dia + hang_nang): (2.696 × 783 + 8.221 × 117) ÷ 900 = 3.414 đ (simulated), khớp hồ sơ.
- Kéo `main` về nhánh `nghongsan` và gộp xung đột ở `TEAM.md`, `ho_so_launch_v0.md` (giữ bảng vai theo phân công, email và GitHub của các thành viên khác).

## 4. Bằng chứng

- Nhánh `nghongsan`, commit `94734dc` (bộ nhãn người 2 trong `report/team/bang_loi.md`).
- Các file: `TEAM.md`, `report/team/bang_loi.md`, báo cáo này.
- Phép tính tay 3.414 đ ở trên; tỉ lệ đồng thuận 17/20 = 85% trong `bang_loi.md`.

## 5. Công cụ AI đã dùng

- Claude Code: đọc cấu trúc repo và đề bài, điền mẫu `TEAM.md`, `ho_so_launch_v0.md` và báo cáo cá nhân, thao tác git (commit, push, merge).
- Tự kiểm tra: đối chiếu từng con số trong hồ sơ với `bang_chi_phi.md` và `bang_loi.md`; kiểm tra nhãn `simulated` và từ cấm bằng `grep`.
- Nhãn lỗi: 20 nhãn do tôi tự gắn, không dùng AI để tạo nhãn (theo RULES.md). Claude Code chỉ chép bộ nhãn tôi đưa vào cột "Nhãn người 2" của `bang_loi.md`.

## 6. Tự đánh giá

- Đã làm: bộ nhãn người 2 (đồng thuận 85%), rà soát và kiểm số hồ sơ, gộp nhánh git, báo cáo cá nhân.
- Cần cải thiện: phối hợp sớm hơn với người điền hồ sơ để không trùng việc (mục 1–7 bị điền hai lần). 