function startEdit(id) {
  document.getElementById('view-' + id).style.display = 'none';
  document.getElementById('edit-' + id).style.display = 'flex';
  const firstInput = document.querySelector('#edit-' + id + ' input');
  if (firstInput) firstInput.focus();
}

function cancelEdit(id) {
  document.getElementById('edit-' + id).style.display = 'none';
  document.getElementById('view-' + id).style.display = 'flex';
}
