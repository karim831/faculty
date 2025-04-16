fs = 10000;
time = 3;
t = linspace(0,time,time*fs);

xn = .1*cos(2*pi*300*t);
sound(xn,fs,16);

figure(1);plot(t,xn),grid;
xlabel('time');
ylabel('amplitude');
title('x(t) reperesentation');
xlim([0,.1]);


xk = abs(fft(xn));
N = fs * time;
f = linspace(0,fs,N);

figure(2); plot(f,xk), grid;
xlabel('frequency');
ylabel('amplitude');
title('x(k) FFT reperesentation');