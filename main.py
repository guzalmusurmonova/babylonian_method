def main(S, d):
    '''create a babylonian function.
    
    Args:
        S (int): number
        d (int): number
        
    Returns:
        float: result
    '''
    a=(S-pow(d,2))/(2*d)
    b=a+d
    x=b-(pow(a,2))/(2*b)

    return x
print(main(16, 4))