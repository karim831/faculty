fs = 10000;
fc1 = 200;
fc2 = 2000;

n = 4; 
#n = 21; 
[b,a] = butter(n,[fc1 fc2]/(fs/2),'bandpass');



figure(1);impz(b,a);
xlabel('SampledTime');
ylabel('Amplitude');
title('Impulse Response');

f = (0:.001:1)*(fs/2);
H = freqz(b,a,f,fs);

figure(2);plot(f,abs(H));
xlabel('Frequency');
ylabel('Amplitude');
title('Frequency Response');
