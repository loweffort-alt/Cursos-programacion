function differenceInAges(ages) {
    // your solution here
  
    {
      let minimo = Math.min.apply(null, ages);
      let maximo = Math.max.apply(null, ages);
      let diferencia = maximo - minimo;
    };
  
    age = [minimo, maximo, diferencia];
  
    return age;
  }
  
  console.log (ages[4, 5, 2, 3])