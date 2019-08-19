% PID Tune the linearized actuator plant

model_parameter_values

% create linear plant
[A,B,C2,D]=linmod('EMA_model_B_PID_tune');
EMA_plant = ss(A,B,C2,D);
EMA_plant_sys = tf(EMA_plant);
figure;bode(EMA_plant_sys)
