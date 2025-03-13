export default function getStudentIdsSum(students) {
  const idsSum = students.reduce((acc, student) => acc + student.id, 0);
  return idsSum;
}
