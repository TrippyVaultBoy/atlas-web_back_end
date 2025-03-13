export default function getStudentIdsSum(students) {
  idsSum = students.reduce((acc, student) => acc + student.id, 0);
  return idsSum;
}
