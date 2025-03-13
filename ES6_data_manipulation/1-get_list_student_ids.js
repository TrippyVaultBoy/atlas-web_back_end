export default function getListStudentIds(students) {
  if (!students.isArray(students)) {
    return [];
  }
  const ids = students.map(student => student.id);
  return ids;
}
