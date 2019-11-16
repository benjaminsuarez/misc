x =[0:10]
y = x.^2+10*x
dy = 2*x + 10

subplot(1,2,1); % divides plot to a 1x2 grid, access first element
plot(x, y);
subplot(1,2,2);
plot(x, dy, 'r')
[x;y;dy]'

clf; % clear

close %close plot
