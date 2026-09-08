# Vietnamese Bilingual Fact-Check & Verification Template
## Mẫu Bảng Đối Soát Sự Thật & Kiểm Định Nội Dung Tiếng Việt

Tài liệu này định nghĩa cấu trúc của **Bảng Đối Soát Sự Thật (Bilingual Fact-Check Dashboard)**. Mỗi khi skill `seo-review-writer` sinh ra bài viết tiếng Anh, nó BẮT BUỘC phải xuất kèm báo cáo đối soát này để chủ website người Việt có thể rà soát và kiểm chứng toàn bộ thông số, luận điểm và khuyến mãi chỉ trong vòng 1-2 phút.

---

## Cấu Trúc Báo Cáo Đối Soát Chuẩn

```markdown
# 🔍 BẢNG ĐỐI SOÁT & KIỂM ĐỊNH NỘI DUNG (FACT-CHECK DASHBOARD)
**Tiêu đề bài viết:** [Tiêu đề tiếng Anh của bài viết]
**Sản phẩm đối soát:** [Tên các model hoặc sản phẩm phân tích]
**Thời gian kiểm định:** [YYYY-MM-DD]
**Người thẩm định đề xuất:** [Tên Author Persona trong bài]

---

### 1. Bảng Đối Soát Thông Số Kỹ Thuật (Ground-Truth Hardware Audit)
*Mục đích: Loại bỏ 100% hiện tượng ảo giác (hallucination) của AI về các con số kỹ thuật.*

| Thông số (Kỹ thuật) | Tuyên bố trong bài tiếng Anh | Dịch nghĩa & Giải thích tiếng Việt | Căn cứ nguồn gốc (Ground Truth) | Trạng thái |
|---|---|---|---|---|
| **Công suất hút (Air Watts)** | "150 AW (V12) vs 240 AW (V15)" | V12 đạt 150 AW, V15 đạt 240 AW (mạnh hơn 60%) | Trang thông số kỹ thuật Dyson Official | ✅ Chính xác 100% |
| **Trọng lượng thân máy** | "5.2 lbs (2.4 kg) vs 6.8 lbs (3.1 kg)" | V12 nhẹ hơn gần 0.7 kg so với V15 | Cân nặng thực tế Dyson Datasheet | ✅ Đã xác minh |
| **Cơ chế công tắc** | "Push-button start vs index-finger trigger" | V12 bấm nút 1 lần là chạy; V15 phải bóp giữ ngón tay | Thiết kế công thái học Dyson | ✅ Đã xác minh |
| **Dung tích hộp chứa bụi** | "0.1 gal (0.38L) vs 0.2 gal (0.76L)" | Hộp rác V15 to gấp đôi V12 | Manual hướng dẫn sử dụng | ✅ Chính xác 100% |
| **Thời lượng pin công bố** | "40-45 mins vs 60 mins Eco mode" | V12 chạy 40-45p, V15 chạy 60p ở chế độ tiết kiệm | Thử nghiệm pin tiêu chuẩn | ✅ Đã xác minh |

---

### 2. Bảng Đối Soát Trải Nghiệm Thực Tế & Đánh Đổi (Real-World Trade-Offs & Consensus)
*Mục đích: Xác thực các luận điểm khen/chê có phản ánh đúng ý kiến cộng đồng (Reddit, YouTube, RTINGS, VacuumWars) hay không.*

| Chủ đề trải nghiệm | Luận điểm bài viết (English Claim) | Tóm tắt tiếng Việt & Trải nghiệm thực tế | Nguồn cộng đồng kiểm chứng | Đánh giá tính trung thực |
|---|---|---|---|---|
| **Độ mỏi cổ tay** | V12 push-button eliminates finger fatigue | V12 không phải giữ ngón tay liên tục, đỡ mỏi rõ rệt khi dọn nhà nhiều tầng | r/dyson: 85% người dùng xác nhận | ⭐⭐⭐⭐⭐ Rất chân thực |
| **Đổ bụi hộc rác** | V12 bin is small and requires wand detachment | Hộc rác V12 nhỏ, khi đổ rác phải tháo thanh nối dài ra mới mở nắp được | Đánh giá người dùng thực tế | ⭐⭐⭐⭐⭐ Chính xác |
| **Hiệu quả trên thảm dày** | V15 acoustic piezo surges on deep pile (94% pickup) | V15 hút sạch hơn hẳn trên thảm lông sâu, tự tăng tốc độ khi gặp nhiều bụi | Benchmark sand embedment test | ⭐⭐⭐⭐⭐ Đã kiểm chứng |
| **Độ bền tia laser** | Green optic beam scratches if dropped on tile | Đầu hút laser quang học nếu va đập mạnh có thể trầy thấu kính | Báo cáo bảo hành sau 1 năm | ⭐⭐⭐⭐ Đáng lưu ý |

---

### 3. Bảng Kiểm Định Mẹo Khuyến Mãi & Voucher (Smart Cart Deal Verification)
*Mục đích: Đảm bảo các cách tiết kiệm tiền nêu trong bài là có thật và khả thi, tạo giá trị thực tế cho độc giả SmartCartVouchers.*

| Mẹo tiết kiệm | Mô tả trong bài viết | Khả thi thực tế (Verification) | Hướng dẫn hành động cho độc giả |
|---|---|---|---|
| **Dyson Owner Rewards (20% Off)** | Giảm 20% cho khách hàng cũ đã đăng ký sản phẩm | Áp dụng chính thức trên Dyson Direct | Đăng nhập tài khoản Dyson hoặc chat với hỗ trợ |
| **Price Match Guarantee** | So khớp giá với Best Buy, Target, Amazon | Dyson cam kết match giá với đại lý ủy quyền | Chat trực tiếp với Dyson live-chat trước khi thanh toán |
| **Free Tool Kit Bundle ($75)** | Tặng kèm đầu hút nệm và chổi quét bụi mềm | Dyson thường xuyên chạy promo tặng phụ kiện | Kiểm tra banner khuyến mãi trên trang chủ Dyson |
| **Hàng Refurbished chính hãng** | Giảm 30-40% hàng tân trang chính hãng trên eBay/Outlet | Hàng chính hãng được bảo hành 1-2 năm | Dẫn link affiliate đến Dyson Outlet Store |

---

### 4. Kết Luận Phê Duyệt Của Webmaster (Approval Sign-off)
* **Chất lượng E-E-A-T**: Đạt (Có thông số thực, có hạn chế thực tế, có thông tin giá trị độc quyền).
* **Tuân thủ Affiliate FTC**: Đã gắn `rel="sponsored nofollow"` và thông báo Affiliate Disclosure ở đầu trang.
* **Thời gian duyệt**: Chỉ mất ~2 phút đọc bảng này thay vì đọc 2,500 từ tiếng Anh!
```
