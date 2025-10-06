#3. 

#1 y[n] =1/8 * (x[n] + x[n − 1] + x[n − 2] + x[n − 3] + x[n − 4] +x[n − 5] + x[n − 6] + x[n − 7])
num = (1/8) * ones(1,8);
denum = 1;

figure(1);impz(num,denum);
xlabel('Discreate Time pins n');
ylabel('Amplitude h');
title('Impulse Response');

fs = 2000;
f = (0:.001:1)*(fs/2);
H = freqz(num,denum,f,fs);

figure(2);plot(f,abs(H));
xlabel('Freqeuncy f');
ylabel('Amplitude |H|');
title('Freqeuncy Response');



#2 y[n] =1/8 * (x[n] − x[n − 8]) + y[n − 1]

num2 = (1/8) * [1 zeros(1,7) -1];
denum2 = [1 -1];

figure(3);impz(num2,denum2);
xlabel('Discreate Time pins n');
ylabel('Amplitude h');
title('Impulse Response');

H2 = freqz(num2,denum2,f,fs);

figure(4);plot(f,abs(H2));
xlabel('Freqeuncy f');
ylabel('Amplitude |H|');
title('Freqeuncy Response');