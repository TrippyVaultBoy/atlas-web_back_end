export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsByLocation = students.filter((student) => student.location === city);
  
  const updatedGrades = studentsByLocation.map((student) => {
    const gradeEntry = newGrades.find((grade) => grade.studentId === student.id)
    const updatedGrade = {
      ...student,
      grade: gradeEntry ? greadeEntry.grade : 'N/A'
    };
    return updatedGrade;
  });
  return updatedGrades;
}
