# prefered to use fs = 8000, 11025,22050, 44100

fs = 44100;
time = 3;

system(sprintf('arecord -d %d -r %d %s',time,fs,'sound/my_sound.wav'));


[x,fs] = audioread('sound/my_sound.wav');

sound(x,fs,16);

