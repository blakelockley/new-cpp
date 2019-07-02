#ifndef MY_CLASS_H
#define MY_CLASS_H

class MyClass {
public:

    MyClass();


    void doStuff();

    int getNum();
    void setNum(int a);

    void lotsOfArgs(int a, float *b, int c);
    
    float getA() { return this-> A; }
    int &someRef();
    int *somePtr();

private:
    int A;

};

#endif