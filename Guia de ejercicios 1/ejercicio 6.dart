void main() {
  List<int> a = [4,3,2,2,1];
  List<int> b = [-3,2,8,0,1]; 
 
  List<int> result =[];

  for (int i = 0; i < a.length; i++) {
    result.add(a[i] * b[i]);
}

print(result);

}