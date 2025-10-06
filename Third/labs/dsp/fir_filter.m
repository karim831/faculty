[xn,fs] = audioread('sound/file1.wav');
n = 50;
fc = 5000;
a = 1;
b = fir1(n,fc/(fs/2),'low');
hn = impz(b,a,n);
figure(1);plot(hn);
f = (0:.001:1)*(fs/2);
H = freqz(b,a,f,fs);
figure(2);plot(f,abs(H)); 

yn = conv(xn,hn,'same');


sound(yn,fs);