function s = poissonarrivals(lam, T)
n = ceil(1.1*lam*T);
s = cumsum(exponentialrv(lam, n));
while (s(length(s))<T),
    s_new = s(length(s))+...
        cumsum(exponentialrv(lam, n));
    s = [s, s_new];
end
s = s(s<=T);