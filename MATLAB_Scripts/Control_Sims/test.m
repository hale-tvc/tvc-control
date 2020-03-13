s = tf('s');
k = 1;
b = 1;
m = 1;

sys = 1/(m*s^2+b*s+k);

step(sys)