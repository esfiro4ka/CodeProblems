import square from './square.js';
import {getTriangleArea} from './myMathModule.js';

const getTriangleSquare = (n) => {
  let h = square(n)/2;
  let result = getTriangleArea(n,h);
  return result;
}

export default getTriangleSquare;
