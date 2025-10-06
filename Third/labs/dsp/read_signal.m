[xn,fs] = audioread('sound/Tom.wav');

sound(xn,fs,16);
time = length(xn)/fs;


t = linspace(0,time,time*fs);
figure(1);plot(t,xn),grid;
xlabel('time');
ylabel('amplitude');
title('x(n) reperesentation');
xlim([0,.1]);


xf = abs(fft(xn));
f = linspace(0,fs,length(xn));
figure(2);plot(f,xf),grid;
xlabel('freq');
ylabel('amplitude');
title('x(f) reperesentation');