// taskFirst : 'task' est déclarée et retournée sans modification
// → on utilise const car la valeur ne change pas
export function taskFirst() {
  const task = 'I prefer const when I can.'; // const : valeur fixe
  return task;
}

// getLast : fonction utilitaire, pas de variable à modifier
export function getLast() {
  return ' is okay';
}

// taskNext : 'combination' est modifiée avec += donc elle est réassignée
// → on utilise let car la valeur change
export function taskNext() {
  let combination = 'But sometimes let'; // let : valeur modifiée ensuite
  combination += getLast(); // réassignation : justifie let
  return combination;
}
