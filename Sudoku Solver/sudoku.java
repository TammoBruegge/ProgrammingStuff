public class SeriousSudokuSolver {
	private static int[][] mySudoku;
	private static final int UNASSIGNED = -1;
	private static int n;

	// Guckt ob ein Eintrag valid wäre
	private static boolean isValid(int row, int col, int number) {
		if (number != UNASSIGNED) {

			// Für die Zeile
			for (int i = 0; i < n * n; i++) {
				if (mySudoku[row][i] == number && i != col) {
					return false;
				}
			}

			// Für die Spalte
			for (int i = 0; i < n * n; i++) {
				if (mySudoku[i][col] == number && i != row) {
					return false;
				}
			}

			// Fürs Kästchen
			int r = row - row % n; // Für die Zeile
			int c = col - col % n; // Für die Spalte

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (mySudoku[i + r][j + c] == number && row != i + r && col != j + c) {
						return false;
					}
				}
			}

			return true;
		}

		return true;
	}

	public static boolean solveSudoku() {

		for (int row = 0; row < n * n; row++) {
			for (int col = 0; col < n * n; col++) {

				if (mySudoku[row][col] == UNASSIGNED) {

					for (int number = 1; number <= n * n; number++) {
						mySudoku[row][col] = number;
						if (!isValid(row, col, number)) {
							mySudoku[row][col] = UNASSIGNED;
						} else {
							if (solveSudoku()) {
								return true;
							} else {
								mySudoku[row][col] = UNASSIGNED;
							}
						}
						// if (isValid(row, col, number)) {
						// mySudoku[row][col] = number;
						//
						// if (solveSudoku()) {
						// return true;
						// } else {
						// mySudoku[row][col] = UNASSIGNED;
						// }
						// }
					}
					return false;
				}
			}
		}
		return true;
	}

	/**
	 * Solves the given Sudoku through backtracking.
	 * 
	 * @param rank
	 *            Determines the size of the Sudoku. A Field of rank n will have n^2
	 *            columns and rows.
	 * @param sudoku
	 *            The start configuration of the Sudoku. Empty cells are initialized
	 *            as -1.
	 * @return The solved Sudoku.
	 * @throws IllegalArgumentException
	 *             if the given Sudoku is impossible to solve.
	 */
	public static int[][] solve(int rank, int[][] sudoku) throws IllegalArgumentException {
		n = rank;
		mySudoku = sudoku;

		// Überprüfun ob gegebenes Sudoku überhaupt valide ist
		for (int i = 0; i < n * n; i++) {
			for (int j = 0; j < n * n; j++) {
				int field = sudoku[i][j];

				if (!isValid(i, j, field)) {
					throw new IllegalArgumentException("Sudoku ist nicht valide.");
				}

			}
		}

		if (rank < 1) {
			throw new IllegalArgumentException("Das Sudoku muss mindestens 1 groß sein");
		} else {
			if (!solveSudoku()) {
				throw new IllegalArgumentException("Sudoku ist nicht lösbar.");
			} else {
				return mySudoku;
			}
		}

	}
}