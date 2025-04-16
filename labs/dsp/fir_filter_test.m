% Read input signal
[xn, fs] = audioread('sound/file1.wav');
sound(xn, fs);

N = length(xn);
time = N/fs;
t = linspace(0, time, N);

% Plot time domain signal
figure(1); plot(t, xn), grid;
xlabel('Time (s)');
ylabel('Amplitude');
title('x(n) - Time Domain');

% Frequency domain of original signal
xk = abs(fft(xn));
f = linspace(0, fs, N);
figure(2); plot(f, xk), grid;
xlabel('Frequency (Hz)');
ylabel('Amplitude');
title('x(f) - Frequency Domain');

% Design a low-pass FIR filter using windowed sinc
cutoff_freq = 4000;  % Set your desired cutoff frequency (Hz)
wc = 2 * pi * (cutoff_freq / fs);  % Normalized cutoff in rad/sample

M = 100;  % Filter length (should be even for symmetric filter)
n = -M/2 : M/2;  % Symmetric time indices

% Ideal sinc-based low-pass filter
fir = wc/pi * sinc(wc * n / pi);
% Apply Hamming window
window = hamming(length(n))';
fir = fir .* window;
% Plot impulse response of the FIR filter
figure(3); plot(n, fir), grid;
xlabel('n'); ylabel('Amplitude'); title('fir(n) - Windowed FIR Filter');

% Frequency response of the FIR filter
FIR = abs(fft(fir, fs));
FIR_f = linspace(0, fs, fs);
figure(4); plot(FIR_f, FIR), grid;
xlabel('Frequency (Hz)');
ylabel('Amplitude');
title('fir(f) - Frequency Response');

% Apply the FIR filter using convolution
yn = conv(xn, fir, 'same');

% Play and plot the output
sound(yn, fs);
figure(5); plot(t, yn), grid;
xlabel('Time (s)');
ylabel('Amplitude');
title('y(n) - Filtered Signal');
