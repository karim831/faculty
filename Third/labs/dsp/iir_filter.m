fs = 8000;
fc = 3000;
n = 5;
[b,a] = butter(n,fc/(fs/2),'low');

figure; impz(b,a);
f = (0:.001:1)*(fs/2);
H = freqz(b,a,f,fs);

figure; plot(f,abs(H));
