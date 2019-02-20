

% Import Impulse data as "Impulse=[...]";

Time=1:1:4000; 
for j=1:4000;
Y1(j)=Impulse(1);
end
Y=(Impulse-Y1')*10^3;
f = fit(Time',Y,'gauss4');

plot (f,Time,Y,'*');

Y2=f(Time);
peak=max(Y2);

X1=find(Y2>0.5*peak,1,'first');
X2=find(Y2>0.5*peak,1,'last');
FWHM=X2-X1;
xlabel('time (ps)') ;
ylabel('Amplitude (mV)') ;
txt = ['FWHM','=',num2str(FWHM),' ', 'ps'];
text(600,0.5*peak,txt);
