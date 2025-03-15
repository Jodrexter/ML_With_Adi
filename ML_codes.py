def null_value_treatment(x):
    for i in x.columns:
        if x[i].dtypes==object:
            x[i]=x[i].fillna(x[i].mode()[0])
        else:
            x[i]=x[i].fillna(x[i].mean())

def cat_con(x):
    cat=[]
    con=[]
    for i in x.columns:
        if x[i].dtypes==object:
            cat.append(i)
        else:
            con.append(i)
    print('cat :',cat)
    print('con :',con)

def outlier(x):
    out = []
    for i in x.columns:
        a = x[(x[i]<-3)|(x[i]>3)].index
        out.extend(a)
    b = list(set(out))
    print('outliers : ',b)


