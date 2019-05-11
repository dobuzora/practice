#include<iostream>
#include<queue>
#include<string>
using namespace std;

int main() {
  queue<string> Q;

  Q.push("red");
  Q.push("yellow");
  Q.push("yellow");
  Q.push("blue");

  cout << Q.front() << " ";
  Q.pop();

  cout << Q.front() << " ";
  Q.pop();

  cout << Q.front() << " ";
  Q.pop();

  Q.push("green");

  cout << Q.front() << " ";
  Q.pop();

  cout << Q.front() << endl;

  return 0;
}
