[xn,fs] = audioread('../sound/whistle.wav');
sound(xn,fs)
# 1- Read the file into MATLAB, specify #samples and time of recording in sec.
N = length(xn); 

time = N/fs;

# 2- Plot the frequency spectrum of signal x, do you notice the peaks?

xk = fft(xn);
f = linspace(0,fs,N);

figure(1);plot(f,abs(xk));
xlabel('Frequency');
ylabel('Amplitude');
title('Frequency spectrum X(f)');

# 3- Design a filter to reject the sinusoidal signals from signal x.

n = 10000;
#first filter
fc1 = 1460;
fc2 = 1530;

a = 1;
b = fir1(n,[fc1 fc2]/(fs/2),'stop');

#second filter
fc3 = 420;
fc4 = 550;

c = 1;
d = fir1(n,[fc3 fc4]/(fs/2),'stop');

#compining them 
bd = conv(b,d,'same');
ac = 1;

# 4- Plot frequency response, impulse response of the designed filter. Is the filter stable?

figure(2); impz(bd,ac);
xlabel('Discreate Time pins n');
ylabel('Amplitude h');
title('Impulse Response FIR Filter');

f = (0:.001:1)*(fs/2);
H = freqz(bd,ac,f,fs);

figure(3); plot(f,abs(H));
xlabel('Frequency f');
ylabel('Amplitude |H|');
title('Frequency Response FIR Filter');

# 5- Plot the frequency spectrum of signal y (the output of the filter).
yn = filter(bd,ac,xn);

yk = fft(yn);
f = linspace(0,fs,N);

figure(4);plot(f,abs(yk));
xlabel('Frequency');
ylabel('Amplitude');
title('Frequency spectrum Y(f)');

# 6- Play the output signal is the whistle still there?
sound(yn,fs);

# 7- Calculate the energy for the original signal and the filtered signal.

ex = sum(abs(xn).^2);

ey = sum(abs(yn).^2);

