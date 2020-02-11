// ex09.cpp
# include <iostream>
# include <cstdlib> // used for generating random number
# include <ctime> // same above
using namespace std;

// hero
class Hero
{
private:
    int power;
public:
    Hero(): power(100){}
    void attack(int n);
    void damage(int n);
};

void Hero::attack(int n)
{
    cout << "attack by Hero" << endl;
    if(power >= n){
        cout << "BOM!!" << endl;
        power -= n;
    }
    else{
        cout << "no happened" << endl;
    }
    cout << "Remaining amount of power : " << power << endl;
}

void Hero::damage(int n)
{
    power -= n;
    if(power > 0){
        cout << "Remaining amount of power : " << power << endl;
        cout << "never giveup!!" << endl;
    }
    else{
        cout << "you lost" << endl;
    }
}

// Boss
class Boss
{
private:
    int power;
public:
    Boss(): power(100){}
    void attack(int n);
    void damage(int n);
    int returnPower();
};

void Boss::attack(int n)
{
    cout << "attack by Boss" << endl;
    if(power >= n){
        cout << "BOM!!" << endl;
        power -= n;
    }
    else{
        cout << "no happened" << endl;
    }
    cout << "Remaining amount of power : " << power << endl;
}

void Boss::damage(int n)
{
    cout << "Are you kidding??" << endl;
    power -= n;
    if(power <= 0){
        cout << "I can`t beleve..." << endl;
        cout << "You win!!" << endl;
    }
    else{
      cout << "Remaining amount of power : " << power << endl;  
    }
}

int Boss::returnPower(){
    return Boss::power;
}

// battle place
class Battle_place
{
private:
    Boss boss;
    Hero hero;
    int boss_place;
    int hero_place;
public:
    Battle_place();
    void battle();
};

Battle_place::Battle_place()
{
    srand((unsigned)time(NULL)); // initialization
    boss_place = rand() % 5 + 1;
    cout << "started your battle against boss" << endl;
    cout << "boss is hiding somewhere in 1-5" << endl;
    cout << "you have hide somewhere in 1-5, which??" << endl;
    cin >> hero_place;
}

void Battle_place::battle()
{
    int point, attacking_power;
    cout << "It`s your turn" << endl;
    cout << "Please enter place number 1-5" << endl;
    cin >> point;
    cout << "Please enter attacking power <100" << endl;
    cin >> attacking_power;
    cout << endl;
    hero.attack(attacking_power);

    if(boss_place == point){
        boss.damage(attacking_power*2);
    }
    else{
        cout << "your attack has falied." << endl;
    }

    cout << endl;
    
    if(boss.returnPower() > 0){
        cout << "It`s boss turn" << endl;
        cout << "Please push the enter key" << endl;

        cin.get();
        cin.sync();
        cin.get();

        point = rand() % 5 + 1;
        attacking_power = rand() % 100 + 1;

        boss.attack(attacking_power);
        if(hero_place == point){
            hero.damage(attacking_power*2);
        }
        else{
            cout << "boss attack has failed" << endl;
        }
    }
    else{
        cout << "you became true HERO!!!";
    }
}

int main()
{
    Battle_place somewhere;
    somewhere.battle();
}