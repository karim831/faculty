fs = 8000;
time = 3;
N = fs*time;
t= linspace(0,time,N);
xn = rand(1,N)*2 -1;

sound(xn,fs,16);

figure(1);plot(t,xn),grid;
xlabel('time');
ylabel('amplitude');
title('x(n) reperesentation');
xlim([0,.1]);



xk = abs(fft(xn));
f = linspace(0,fs,N);

figure(2); plot(f,xk), grid;
xlabel('frequency');
ylabel('amplitude');
title('x(k) FFT reperesentation');