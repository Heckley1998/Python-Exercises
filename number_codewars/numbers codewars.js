var final_total =[];
var number =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15];
var i;
var positive_total = 0;
var negative_total = 0;
for (i = 0; i < number.length; i++) {
    if (number[i] > 0) {
        positive_total += 1;
        
    }
    else if (number[i] < 0) {

    
        negative_total += number[i];
    }
    else if (number.length == 0){
        final_total = [positive_total, negative_total];
        return final_total;
    }
    else
    {return 'invalid input';}
    
    
}
