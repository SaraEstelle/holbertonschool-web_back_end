const kClass = Symbol('kClass');

export default class Car {
    constructor(brand, motor, color) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;

        this[kClass] = new.target;
    }

    cloneCar() {
        const Cls = this[kClass];
        return new Cls(this._brand, this._motor, this._color);
    }
}
