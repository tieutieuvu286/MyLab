program cv_dt_hinh_tron;
uses crt;
const
	PI = 3.14;
var bankinh, chuvi, dientich: real;
begin
	write('Nhap ban kinh hinh tron: ');
	readln(bankinh);
	chuvi := 2 * PI * bankinh;
	dientich := PI * bankinh * bankinh;
	writeln('Chu vi hinh tron: ', chuvi:1:1);
	writeln('Dien tich hinh tron: ', dientich:1:1);
	readln;
end.
