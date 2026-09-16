/*
 * build_vb_dang.js — dựng văn bản THỂ THỨC ĐẢNG cho cá nhân đảng viên (docx-js).
 * Quy ước: reference/van-ban-dang-ca-nhan.md (Bạn chốt 16/9/2026).
 * Cách dùng: sửa NGUOI, CHI_BO, nội dung 3 văn bản mẫu (f1 giải trình tiếp thu, f2 kế hoạch khắc phục,
 * f3 báo cáo kết quả khắc phục) rồi `node build_vb_dang.js`. Nội dung dưới là VÍ DỤ, đã thay tên thật bằng tên giả.
 * Hàm dùng lại: header(ngày) — góc trái/phải + gạch dưới cân; kg(lines, off) — khối Kính gửi thẳng cột, cân giữa;
 * sign() — khối ký cá nhân cantSplit; P/C/L/H1 — đoạn thân lùi 1,27 cm đồng đều.
 */
const NGUOI='Nguyễn Văn A'; const CHI_BO='2'; const CHUC_VU='Trưởng phòng X'; const PHONG='Phòng X';
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, AlignmentType, Table, TableRow, TableCell, WidthType, BorderStyle, VerticalAlign, TabStopType } = require('docx');
const F='Times New Roman', SZ=28, PURPLE='7030A0';
const run = r => { if (typeof r==='string') r={text:r}; return new TextRun({text:r.text,bold:r.bold,italics:r.italics,underline:r.ul?{}:undefined,color:r.purple?PURPLE:undefined,font:F,size:r.size||SZ}); };
const P=(runs,o={})=>new Paragraph({keepNext:o.keep,alignment:o.align||AlignmentType.JUSTIFIED,spacing:{before:0,after:o.after??80,line:o.line||320},indent:o.flush?undefined:{firstLine:720},children:(Array.isArray(runs)?runs:[runs]).map(run)});
const C=(runs,o={})=>P(runs,{...o,align:AlignmentType.CENTER,flush:true});
const L=(runs,o={})=>P(runs,{...o,align:AlignmentType.LEFT,flush:true});
const NB={style:BorderStyle.NONE,size:0,color:'FFFFFF'};
const noB={top:NB,bottom:NB,left:NB,right:NB};

function header(d){
  const cell=(w,ch)=>new TableCell({width:{size:w,type:WidthType.DXA},borders:noB,children:ch});
  return new Table({columnWidths:[4300,5000],width:{size:9300,type:WidthType.DXA},rows:[new TableRow({children:[
    cell(4300,[C([{text:'ĐẢNG BỘ SỞ CÔNG THƯƠNG TỈNH LÀO CAI',size:26}],{after:0,line:276}),
      C([{text:'CHI BỘ SỐ '+CHI_BO+'',bold:true,size:26}],{after:0,line:276}),
      C([{text:'*',size:26}],{after:0,line:276})]),
    cell(5000,[C([{text:'ĐẢNG CỘNG SẢN VIỆT NAM',bold:true,size:26}],{after:0,line:276}),
      new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:0},border:{top:{style:BorderStyle.SINGLE,size:6,color:'000000',space:1}},indent:{left:880,right:1020},children:[]}),
      C([{text:'Lào Cai, '+d,italics:true,size:26}],{after:0,line:276})]),
  ]})]});
}
function sign(){
  const cell=(w,ch)=>new TableCell({width:{size:w,type:WidthType.DXA},borders:noB,children:ch});
  return new Table({columnWidths:[4300,5000],width:{size:9300,type:WidthType.DXA},rows:[new TableRow({cantSplit:true,children:[
    cell(4300,[L([{text:'Nơi nhận:',bold:true,italics:true,size:24}],{after:0,line:276}),
      L([{text:'- Như trên;',size:22}],{after:0,line:276}),
      L([{text:'- Đảng ủy Sở Công thương;',size:22}],{after:0,line:276}),
      L([{text:'- Chi ủy Chi bộ số '+CHI_BO+';',size:22}],{after:0,line:276}),
      L([{text:'- Lưu: cá nhân.',size:22}],{after:0,line:276})]),
    cell(5000,[C([{text:'NGƯỜI BÁO CÁO',bold:true}],{after:0}),C('',{after:0}),C('',{after:0}),C('',{after:0}),C([{text:''+NGUOI+'',bold:true}],{after:0})]),
  ]})]});
}
const mk=(children)=>new Document({styles:{default:{document:{run:{font:F,size:SZ}}}},sections:[{properties:{page:{margin:{top:1134,bottom:1134,left:1701,right:1134}}},children}]});
const kg=(lines,off=3760)=>{const out=[new Paragraph({alignment:AlignmentType.LEFT,spacing:{after:0,line:320},indent:{left:off,hanging:1560},tabStops:[{type:TabStopType.LEFT,position:off}],children:[run({text:'Kính gửi:\t'}),run(lines[0])]})];for(let i=1;i<lines.length;i++)out.push(new Paragraph({alignment:AlignmentType.LEFT,spacing:{after:i===lines.length-1?240:0,line:320},indent:{left:off},children:[run(lines[i])]}));return out;};
const H1=(t)=>P([{text:t,bold:true}],{noIndent:true});
const D=(t)=>P(t,{noIndent:true});

/* ================= FILE 1: BÁO CÁO GIẢI TRÌNH, TIẾP THU ================= */
const f1=mk([header('ngày 16 tháng 9 năm 2026'),C('',{after:0}),
 C([{text:'BÁO CÁO',bold:true}],{after:0}),
 C([{text:'Giải trình, tiếp thu dự thảo Báo cáo kết quả giám sát',bold:true}],{after:0}),C([{text:'của Đoàn giám sát Ban Thường vụ Đảng ủy UBND tỉnh',bold:true}],{after:0}),
 C([{text:'(theo Quyết định số 580-QĐ/ĐU ngày 07/8/2026',italics:true}],{after:0}),C([{text:'của Ban Thường vụ Đảng ủy UBND tỉnh)',italics:true}],{after:240}),
 ...kg([{text:'Đoàn giám sát theo Quyết định số 580-QĐ/ĐU'},{text:'ngày 07/8/2026 của Ban Thường vụ Đảng ủy UBND tỉnh.'}],2500),
 P([{text:'Thực hiện Quyết định số 580-QĐ/ĐU ngày 07/8/2026 của Ban Thường vụ Đảng ủy Ủy ban nhân dân tỉnh về giám sát đối với 04 đảng viên thuộc Đảng bộ Sở Công thương tỉnh Lào Cai (mốc thời gian giám sát từ ngày 01/7/2025 đến ngày 30/6/2026); sau khi nghiên cứu dự thảo Báo cáo kết quả giám sát của Đoàn giám sát, tôi là '+NGUOI+', Ủy viên Ban Chấp hành Đảng bộ, '+CHUC_VU+', đảng viên Chi bộ số '+CHI_BO+', xin báo cáo giải trình, tiếp thu như sau:'}]),
 H1('I. Về việc chấp hành quyết định, kế hoạch giám sát'),
 P('Bản thân đã chấp hành nghiêm Quyết định số 580-QĐ/ĐU và Kế hoạch của Đoàn giám sát; xây dựng báo cáo tự giám sát đúng đề cương, đúng thời hạn; cung cấp đầy đủ hồ sơ, tài liệu và làm việc trực tiếp với Đoàn giám sát theo yêu cầu.'),
 H1('II. Ý kiến đối với dự thảo Báo cáo kết quả giám sát'),
 P([{text:'1. Về phần ưu điểm (mục B.I.2 dự thảo Báo cáo):',bold:true},{text:' Nhất trí với nội dung đánh giá. Dự thảo đã phản ánh đúng, sát thực tế công tác của bản thân trên cả ba nội dung giám sát, ở cả hai vị trí công tác trong mốc thời gian giám sát: Trưởng phòng Kế hoạch - Tổng hợp (từ tháng 7/2025 đến tháng 02/2026) và '+CHUC_VU+' (từ tháng 3/2026 đến nay); ghi nhận đúng các kết quả cụ thể về hoạch định chiến lược, quy hoạch, xây dựng Đề án phát triển công nghiệp, thẩm định dự án, tổng hợp báo cáo; về quản lý cụm công nghiệp, vật liệu nổ công nghiệp, khoa học - công nghệ, phòng chống thiên tai và số lượng văn bản, thủ tục hành chính đã tham mưu.'}],{noIndent:true}),
 P([{text:'2. Về phần hạn chế, khuyết điểm và nguyên nhân (mục B.II.2):',bold:true},{text:' Nhất trí và nghiêm túc tiếp thu toàn bộ hai hạn chế, khuyết điểm được chỉ ra:'}],{noIndent:true}),
 P('- Trong công tác tự phê bình và phê bình với đồng chí, đồng nghiệp, đôi khi chưa thực sự mạnh dạn, thiếu quyết liệt.',{noIndent:true}),
 P('- Thực hiện nhiệm vụ ở lĩnh vực mới, chưa thường xuyên và chưa dành nhiều thời gian nghiên cứu sâu các văn bản, cập nhật văn bản quy phạm pháp luật mới ban hành, nên có việc tham mưu còn hạn chế.',{noIndent:true}),
 P('Về nguyên nhân, bản thân thống nhất với các nguyên nhân khách quan dự thảo đã phân tích (được điều động qua nhiều vị trí trong thời gian ngắn; mô hình chính quyền địa phương 02 cấp và tổ chức bộ máy sau hợp nhất còn mới; hệ thống văn bản quy phạm pháp luật thuộc lĩnh vực Phòng quản lý thay đổi nhiều, hướng dẫn chưa kịp thời, đầy đủ). Tuy nhiên, bản thân xác định nguyên nhân chủ quan là chính: chưa sắp xếp thời gian khoa học để cân đối giữa giải quyết công việc thường xuyên với nghiên cứu, cập nhật quy định; trong sinh hoạt và điều hành có lúc còn nể nang, chưa thẳng thắn góp ý ngay khi đồng chí, đồng nghiệp có việc làm chưa tốt. Bản thân nhận trách nhiệm đầy đủ về các hạn chế nêu trên.'),
 P([{text:'3. Về phần nhận xét, kiến nghị (mục C):',bold:true},{text:' Nhất trí với nhận xét chung và kiến nghị của Đoàn giám sát đối với cá nhân tại mục C.II.2. Bản thân không có ý kiến đề nghị chỉnh sửa, bổ sung đối với các nội dung liên quan đến cá nhân trong dự thảo Báo cáo.'}],{noIndent:true}),
 H1('III. Phương hướng khắc phục'),
 P('Ngay sau khi Ban Thường vụ Đảng ủy UBND tỉnh ban hành Thông báo kết luận giám sát, bản thân sẽ xây dựng Kế hoạch khắc phục hạn chế, khuyết điểm bằng văn bản, báo cáo Đảng ủy Sở và Chi bộ; tập trung vào các nội dung:'),
 P('1. Về tự phê bình và phê bình: gương mẫu tự phê bình trước; thẳng thắn nhận xét, góp ý từng công chức trong Phòng về chất lượng, tiến độ công việc tại các cuộc kiểm điểm tiến độ hằng tuần, hằng tháng; mạnh dạn nêu quan điểm tại các kỳ họp Ban Chấp hành Đảng bộ đối với những vấn đề khó, còn ý kiến khác nhau.',{noIndent:true}),
 P('2. Về nghiên cứu, cập nhật văn bản: bố trí thời gian cố định hằng tuần nghiên cứu văn bản mới thuộc các lĩnh vực Phòng quản lý, ưu tiên nhiệm vụ mới về địa chất, khoáng sản, khu công nghiệp mà Sở tiếp nhận từ ngày 15/9/2026 theo Nghị quyết số 66.25/2026/NQ-CP của Chính phủ; chỉ đạo Phòng lập danh mục văn bản quy phạm pháp luật theo từng lĩnh vực, phân công chuyên viên theo dõi, cập nhật; tổ chức sinh hoạt chuyên môn hằng tháng phổ biến văn bản mới.',{noIndent:true}),
 P('3. Báo cáo kết quả khắc phục với Đảng ủy Sở và Ban Thường vụ Đảng ủy UBND tỉnh theo đúng thời hạn tại Thông báo kết luận giám sát; đưa kết quả khắc phục vào bản kiểm điểm, đánh giá xếp loại đảng viên, công chức năm 2026.',{noIndent:true}),
 P('Bản thân xin nghiêm túc tiếp thu ý kiến đánh giá của Đoàn giám sát và cam kết phát huy ưu điểm, khắc phục có hiệu quả hạn chế, khuyết điểm đã được chỉ ra.'),
 P('Trên đây là Báo cáo giải trình, tiếp thu dự thảo Báo cáo kết quả giám sát, kính báo cáo Đoàn giám sát xem xét, tổng hợp./.',{after:240,keep:true}),
 sign()]);

/* ================= FILE 2: KẾ HOẠCH KHẮC PHỤC ================= */
const cb={top:{style:BorderStyle.SINGLE,size:4,color:'000000'},bottom:{style:BorderStyle.SINGLE,size:4,color:'000000'},left:{style:BorderStyle.SINGLE,size:4,color:'000000'},right:{style:BorderStyle.SINGLE,size:4,color:'000000'}};
const tc=(w,runs,o={})=>new TableCell({width:{size:w,type:WidthType.DXA},borders:cb,verticalAlign:VerticalAlign.CENTER,margins:{top:60,bottom:60,left:80,right:80},children:(Array.isArray(runs)&&Array.isArray(runs[0])?runs:[runs]).map(rs=>new Paragraph({alignment:o.center?AlignmentType.CENTER:AlignmentType.JUSTIFIED,spacing:{after:0,line:250},children:(Array.isArray(rs)?rs:[rs]).map(r=>{if(typeof r==='string')r={text:r};return run({...r,size:24,bold:o.bold||r.bold});})}))});
const W=[600,2100,3700,1400,1500];
const hdr=new TableRow({tableHeader:true,children:[tc(W[0],'TT',{center:true,bold:true}),tc(W[1],'Hạn chế, khuyết điểm',{center:true,bold:true}),tc(W[2],'Giải pháp khắc phục',{center:true,bold:true}),tc(W[3],'Thời gian thực hiện',{center:true,bold:true}),tc(W[4],'Kết quả, sản phẩm để đánh giá',{center:true,bold:true})]});
const r1=new TableRow({children:[tc(W[0],'1',{center:true}),tc(W[1],'Trong công tác tự phê bình và phê bình với đồng chí, đồng nghiệp, đôi khi chưa thực sự mạnh dạn, thiếu quyết liệt.'),
 tc(W[2],[['- Gương mẫu tự phê bình trước tại sinh hoạt chi bộ, họp phòng; thẳng thắn nhận xét từng Phó Trưởng phòng, chuyên viên về chất lượng, tiến độ công việc; nêu rõ việc chưa đạt, yêu cầu và thời hạn khắc phục.'],['- Duy trì kiểm điểm tiến độ hằng tuần, hằng tháng theo Thông báo phân công nhiệm vụ của Phòng; kết quả kiểm điểm là căn cứ đánh giá, xếp loại công chức hằng quý.'],['- Mạnh dạn tham gia ý kiến, nêu rõ quan điểm cá nhân tại các kỳ họp Ban Chấp hành Đảng bộ đối với vấn đề khó, còn ý kiến khác nhau.']]),
 tc(W[3],[[{text:'Từ tháng 9/2026'}],['và thường xuyên']],{center:true}),tc(W[4],[['- Biên bản, sổ ghi kiểm điểm tiến độ hằng tuần, hằng tháng của Phòng.'],['- Ý kiến góp ý được ghi trong biên bản sinh hoạt chi bộ, họp Đảng ủy.'],['- Kết quả đánh giá công chức hằng quý.']])]});
const r2=new TableRow({children:[tc(W[0],'2',{center:true}),tc(W[1],'Thực hiện nhiệm vụ ở lĩnh vực mới, chưa thường xuyên và chưa dành nhiều thời gian nghiên cứu sâu các văn bản, cập nhật văn bản quy phạm pháp luật mới ban hành, có việc tham mưu còn hạn chế.'),
 tc(W[2],[['- Bố trí thời gian cố định hằng tuần để nghiên cứu văn bản mới thuộc các lĩnh vực Phòng quản lý (cụm công nghiệp, khu công nghiệp, vật liệu nổ công nghiệp, hóa chất, khoáng sản, an toàn thực phẩm, môi trường công nghiệp); ưu tiên nhiệm vụ mới về địa chất, khoáng sản, khu công nghiệp Sở tiếp nhận từ 15/9/2026 theo Nghị quyết số 66.25/2026/NQ-CP.'],['- Chỉ đạo Phòng lập, duy trì danh mục văn bản quy phạm pháp luật còn hiệu lực theo từng lĩnh vực; phân công chuyên viên phụ trách lĩnh vực theo dõi, cập nhật, báo cáo Lãnh đạo Phòng ngay khi có văn bản mới.'],['- Tổ chức sinh hoạt chuyên môn hằng tháng tại Phòng để phổ biến, thống nhất cách áp dụng văn bản mới.'],['- Việc khó, hướng dẫn chưa đầy đủ: chủ động trao đổi với các sở, ngành, xin ý kiến Bộ Công Thương; kịp thời báo cáo Đảng ủy, Lãnh đạo Sở xin chủ trương trước khi tham mưu.']]),
 tc(W[3],[[{text:'Từ tháng 9/2026'}],['và thường xuyên; danh mục văn bản hoàn thành trong '],[{text:'tháng 10/2026'}]],{center:true}),tc(W[4],[['- Danh mục văn bản quy phạm pháp luật theo lĩnh vực, được cập nhật hằng tháng.'],['- Biên bản sinh hoạt chuyên môn hằng tháng.'],['- Văn bản tham mưu bảo đảm đúng quy định, đúng tiến độ; không có văn bản phải trả lại do áp dụng sai quy định.']])]});
const f2=mk([header('ngày      tháng      năm 2026'),C('',{after:0}),
 C([{text:'KẾ HOẠCH',bold:true}],{after:0}),
 C([{text:'Khắc phục hạn chế, khuyết điểm sau giám sát',bold:true}],{after:0}),C([{text:'của Ban Thường vụ Đảng ủy UBND tỉnh',bold:true}],{after:240}),
 P([{text:'Căn cứ Quyết định số 580-QĐ/ĐU ngày 07/8/2026 của Ban Thường vụ Đảng ủy Ủy ban nhân dân tỉnh về giám sát đối với 04 đảng viên thuộc Đảng bộ Sở Công thương tỉnh Lào Cai;'}]),
 P('Căn cứ Báo cáo kết quả giám sát ngày 16/9/2026 của Đoàn giám sát và Thông báo kết luận giám sát của Ban Thường vụ Đảng ủy Ủy ban nhân dân tỉnh đối với 04 đảng viên thuộc Đảng bộ Sở Công thương tỉnh Lào Cai;'),
 P('Tôi là '+NGUOI+', Ủy viên Ban Chấp hành Đảng bộ, '+CHUC_VU+' Sở Công thương, xây dựng Kế hoạch khắc phục hạn chế, khuyết điểm được chỉ ra qua giám sát như sau:'),
 H1('I. Mục đích, yêu cầu'),
 P('1. Khắc phục kịp thời, thực chất các hạn chế, khuyết điểm được Đoàn giám sát chỉ ra và Ban Thường vụ Đảng ủy UBND tỉnh kết luận; qua đó nâng cao chất lượng thực hiện chức trách, nhiệm vụ của Ủy viên Ban Chấp hành Đảng bộ, '+CHUC_VU+'.',{noIndent:true}),
 P('2. Giải pháp cụ thể, rõ việc, rõ thời gian, rõ kết quả để chi bộ, Đảng ủy Sở theo dõi, giám sát; kết quả khắc phục là căn cứ kiểm điểm, đánh giá xếp loại đảng viên, công chức năm 2026.',{noIndent:true}),
 H1('II. Nội dung, giải pháp, thời gian khắc phục'),
 new Table({columnWidths:W,width:{size:9300,type:WidthType.DXA},rows:[hdr,r1,r2]}),
 C('',{after:0}),
 H1('III. Tổ chức thực hiện'),
 P('1. Bản thân trực tiếp thực hiện các giải pháp nêu tại mục II; tự theo dõi, lưu giữ minh chứng kết quả khắc phục.',{noIndent:true}),
 P([{text:'2. Báo cáo Kế hoạch này với Chi bộ số '+CHI_BO+' tại kỳ sinh hoạt gần nhất và với Đảng ủy Sở Công thương để theo dõi, giúp đỡ; báo cáo kết quả thực hiện tại kỳ họp Ban Chấp hành Đảng bộ Sở.'}],{noIndent:true}),
 P([{text:'3. Báo cáo kết quả khắc phục bằng văn bản gửi Đảng ủy Sở Công thương và Ban Thường vụ Đảng ủy UBND tỉnh đúng thời hạn quy định tại Thông báo kết luận giám sát; đồng thời thể hiện kết quả khắc phục trong bản kiểm điểm cá nhân cuối năm 2026.'}],{noIndent:true}),
 P('Trên đây là Kế hoạch khắc phục hạn chế, khuyết điểm sau giám sát, kính báo cáo Ban Thường vụ Đảng ủy UBND tỉnh, Đảng ủy Sở Công thương và Chi bộ theo dõi, giám sát./.',{after:240,keep:true}),
 sign()]);

/* ================= FILE 3: BÁO CÁO KẾT QUẢ KHẮC PHỤC ================= */
const f3=mk([header('ngày      tháng      năm 2026'),C('',{after:0}),
 C([{text:'BÁO CÁO',bold:true}],{after:0}),
 C([{text:'Kết quả khắc phục hạn chế, khuyết điểm sau giám sát',bold:true}],{after:0}),C([{text:'của Ban Thường vụ Đảng ủy UBND tỉnh',bold:true}],{after:240}),
 ...kg([{text:'- Ban Thường vụ Đảng ủy UBND tỉnh;'},{text:'- Đảng ủy Sở Công thương tỉnh Lào Cai.'}]),
 P('Thực hiện Thông báo kết luận giám sát của Ban Thường vụ Đảng ủy UBND tỉnh đối với 04 đảng viên thuộc Đảng bộ Sở Công thương tỉnh Lào Cai và Kế hoạch khắc phục hạn chế, khuyết điểm của cá nhân, tôi là '+NGUOI+', Ủy viên Ban Chấp hành Đảng bộ, '+CHUC_VU+', đảng viên Chi bộ số '+CHI_BO+', báo cáo kết quả khắc phục như sau:'),
 H1('I. Hạn chế, khuyết điểm được kết luận qua giám sát'),
 P('1. Trong công tác tự phê bình và phê bình với đồng chí, đồng nghiệp, đôi khi chưa thực sự mạnh dạn, thiếu quyết liệt.'),
 P('2. Thực hiện nhiệm vụ ở lĩnh vực mới, chưa thường xuyên và chưa dành nhiều thời gian nghiên cứu sâu các văn bản, cập nhật văn bản quy phạm pháp luật mới ban hành, có việc tham mưu còn hạn chế.'),
 H1('II. Kết quả khắc phục'),
 P([{text:'1. Về công tác tự phê bình và phê bình',bold:true}]),
 P('Bản thân đã gương mẫu tự phê bình trước tập thể tại các kỳ sinh hoạt chi bộ và họp phòng; trực tiếp nhận xét, góp ý thẳng thắn đối với từng Phó Trưởng phòng, chuyên viên về chất lượng, tiến độ công việc tại các cuộc kiểm điểm tiến độ hằng tuần, hằng tháng; những việc chậm tiến độ, chất lượng chưa đạt đều được chỉ rõ người, rõ nguyên nhân, rõ thời hạn khắc phục và đã được khắc phục.'),
 P('Đã duy trì nghiêm chế độ kiểm điểm tiến độ hằng tuần, hằng tháng theo Thông báo phân công nhiệm vụ của Phòng; kết quả kiểm điểm được sử dụng làm căn cứ đánh giá, xếp loại công chức hằng quý, bảo đảm công tâm, khách quan.'),
 P('Tại các kỳ họp Ban Chấp hành Đảng bộ, đã chủ động tham gia ý kiến, nêu rõ quan điểm cá nhân đối với những vấn đề khó, còn ý kiến khác nhau, với tinh thần xây dựng, vì việc chung; không còn tình trạng nể nang, góp ý chung chung.'),
 P([{text:'2. Về nghiên cứu, cập nhật văn bản quy phạm pháp luật và nâng cao chất lượng tham mưu',bold:true}]),
 P('Đã bố trí thời gian cố định hằng tuần để nghiên cứu các văn bản mới ban hành thuộc các lĩnh vực Phòng quản lý (cụm công nghiệp, khu công nghiệp, vật liệu nổ công nghiệp, hóa chất, khoáng sản, an toàn thực phẩm, môi trường công nghiệp), trọng tâm là các quy định về địa chất, khoáng sản và khu công nghiệp mà Sở tiếp nhận từ ngày 15/9/2026 theo Nghị quyết số 66.25/2026/NQ-CP của Chính phủ.'),
 P('Đã chỉ đạo Phòng xây dựng và duy trì danh mục văn bản quy phạm pháp luật còn hiệu lực theo từng lĩnh vực; phân công chuyên viên phụ trách lĩnh vực theo dõi, cập nhật và báo cáo Lãnh đạo Phòng ngay khi có văn bản mới, kèm đề xuất nội dung cần triển khai, điều chỉnh trong tham mưu.'),
 P('Đã tổ chức sinh hoạt chuyên môn hằng tháng tại Phòng để phổ biến, trao đổi văn bản mới, thống nhất cách hiểu, cách áp dụng, qua đó nâng cao trình độ chung của Phòng và giúp bản thân nắm chắc quy định ở các lĩnh vực mới.'),
 P('Chất lượng tham mưu được nâng lên: các văn bản Phòng tham mưu từ sau giám sát đến nay bảo đảm đúng quy định, đúng tiến độ; hồ sơ thủ tục hành chính được giải quyết đúng và trước hạn; không có văn bản bị trả lại do áp dụng sai quy định. Đối với những việc khó, hướng dẫn chưa đầy đủ, bản thân đã chủ động trao đổi với các sở, ngành liên quan, xin ý kiến Bộ Công Thương và báo cáo Đảng ủy, Lãnh đạo Sở xin chủ trương trước khi tham mưu.'),
 H1('III. Tự đánh giá và phương hướng tiếp theo'),
 P('1. Tự đánh giá: Các hạn chế, khuyết điểm được kết luận qua giám sát đã được khắc phục nghiêm túc, có kết quả; những nội dung có tính thường xuyên (tự phê bình và phê bình, nghiên cứu, cập nhật văn bản) được duy trì thành nền nếp công tác của bản thân và của Phòng.'),
 P('2. Phương hướng: Tiếp tục thực hiện nghiêm các giải pháp tại Kế hoạch khắc phục; đưa kết quả khắc phục vào bản kiểm điểm, đánh giá xếp loại đảng viên, công chức năm 2026; kính đề nghị Đảng ủy Sở và Chi bộ tiếp tục theo dõi, giám sát, giúp đỡ.'),
 P('Trên đây là Báo cáo kết quả khắc phục hạn chế, khuyết điểm sau giám sát, kính báo cáo Ban Thường vụ Đảng ủy UBND tỉnh và Đảng ủy Sở Công thương xem xét./.',{after:240,keep:true}),
 sign()]);

const O=process.env.OUT||'./';
Promise.all([Packer.toBuffer(f1),Packer.toBuffer(f2),Packer.toBuffer(f3)]).then(([a,b,c])=>{
 fs.writeFileSync(O+'2026.09.16. Báo cáo giải trình tiếp thu dự thảo Báo cáo kết quả giám sát - '+NGUOI+'.docx',a);
 fs.writeFileSync(O+'2026.09.16. Kế hoạch khắc phục hạn chế khuyết điểm sau giám sát - '+NGUOI+'.docx',b);
 fs.writeFileSync(O+'2026.09.16. Báo cáo kết quả khắc phục hạn chế khuyết điểm sau giám sát - '+NGUOI+'.docx',c);
 
});
