import 'dart:math';

void main() {
  List<List<int>> lists = List.generate(3, (index) => List.generate(7, (index) => Random().nextInt(70) + 30));
  List<double> averages = [];

  for (var list in lists) {
    int sum = list.reduce((a, b) => a + b);
    double avg = sum / list.length;
    averages.add(avg);
  }

  print(averages);

}



//fin