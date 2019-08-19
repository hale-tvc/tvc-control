% Constant Vehicle Parameters and Conversions
d2r = pi/180; % deg -> rad
r2d = 1/d2r; % rad -> deg
f2m = 0.3048;           % f -> m
lbf2N = 4.44822162825;  % lbf -> N
fp2Nm = 1.35581795;
lbm2kg = 1/2.2046217; % lbm -> kg
lbm_in2kg_m2 = 0.000292641; % lbm-in^2 -> kg-m^2

XX = 1000000; % set a dummy value

%% EMA_model_B parameters
% Provided 7/19/2016 by Tom Quartararo <tom@ultramotion.com> via email
J_m = 34.8*10e-7;                       % [g*cm^2] to [kg*m^2] %	motor inertia (slug-ft2)
N_gear = 4.8/1;                         % motor to screw gear ratio
N_screw = (0.125/12)*f2m/(2*pi);        % [in/rev] to [m/rad] % 	shaft screw ratio (ft/rad) 0.125; % [in/rev]
J_a = 100*10e-7;                        % [g-cm^2] to [kg*m^2]  % 	combined inertia of the gears plus the screw
K_gs = XX;                              % gear stiffness in (ft-lb/rad)
K_C = 0.06;  %disabled in sim - doesnt matter                           % [Nm]      %	motor Coulomb Friction (ft-lb)

%% Parameter values not provided

w_m = 2*pi*1;                           % motor bandwidth in (rad/sec) - not needed with alternate motor representation
%K_mfr =  N/A                           % motor gear damping friction, (ft-lb/rad/sec) due to relative speed
K_md = 0.01712/16/12/0.104719755*fp2Nm; % [oz-in/rpm_rotor] to [Nm/rad/sec] motor viscous damping coefficient (ft-lb/rad/sec) 
%K_mfr = 0.01712;                       % [oz-in/rpm_rotor] % use Kmd	
K_dmp = K_C/1000;                       % shaft friction (ft-lb/rad/sec)
K_eff = 1;                              % efficiency
K_L = XX;                               % backup structure and load stiffness
K_T = XX;                               % total system stiffness
noz2act = 2.769/10;                     % [in/deg] % actuator travel per degree of 2nd stage nozzle deflection
act2noz = 1/noz2act;                    % [deg/in]
R = noz2act/12*f2m/d2r;                 % [in/deg] to [m/rad] nozzle degrees to actuator length ratio, % moment arm, shaft to hinge (ft)
R_moment_arm = 0.3886;                  % moment arm, shaft to hinge (ft)
%J_e = 84007 * lbm_in2kg_m2;            % nozzle pitch inertia about CG, lbm*in^2
J_e = 42.513;                           % load moment of inertia of engine about pivot, kg*m^2
l_noz = 28.4 * f2m/12;                  % length nozzle pivot to noz cg, in
T_L = 130*lbf2N*0.3886;                 % External (static) Torque, (Nm)
V_lim = 28;                             % Voltage Limit, volt
%K_v =                                  % Motor Torque Gain (ft-lb/volt)

K_t = 1.92/16/12/fp2Nm;                 % [oz-in/A_rms] to [Nm/A] motor current to torque constant (ft-lb/amps)	 1.92 oz-in/A_rms
R_m = 0.102;                            % motor winding resistance in (ohms)	 0.102 ? phase to phase
T_m = 1/1000;                           % motor time constant in (seconds)	
K_emf = 1.429/0.104719755/1000;         % motor back-emf gain (volt/rad/sec)	1.429 V/krpm



%% Design-to parameters

% Design 1 - works well for maximum step response speed, and ok freq
% response
K_i = 0;               %	integral gain
K_p = 10000;               %	position gain
K_r = 0.03;               % 	rate gain

%% TRY USING PID TUNE
% 

% From PID tune
% attempt 1 - PID, nulled Ki in simulink
C.Kp = -5.22e+03;
C.Ki = -1.55e+04;
C.Kd = -122;
 
% attempt 2 - just PD
C.Kp = -1.89e+04;
C.Kd = -272;
C.Ki = 0;