export default function hasValueFromArray(set, array) {
    return array.every((val) => set.has(val));
}
