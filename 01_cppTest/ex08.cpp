// ex08.cpp
# include <iostream>
# include <string>
using namespace std;

class Glass
{
private:
    int amount;
public:
    Glass() : amount(10){}
    void PutOut(){ 
        amount -= 2;
        cout << "water amount in this glass = " << amount << endl;
    }
};

int main()
{
    Glass glass;

    cout << "created glass of Glass" << endl;
    cout << "putting out water from glass" << endl;
    glass.PutOut();
    cout << "finish" << endl;
}