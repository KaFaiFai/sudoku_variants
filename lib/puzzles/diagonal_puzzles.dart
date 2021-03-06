import '../model/sudoku_board.dart';
import '../model/sudoku_puzzle.dart';
import '../model/sudoku_variation.dart';

final sudokuDiagonalPuzzle = [
  SudokuPuzzle(
    initialBoard: SudokuBoard.fromString(".8.....9."
        "5.3...8.2"
        ".4.1.2.6."
        "..1.3.4.."
        "...4.1..."
        "..4.6.5.."
        ".2.7.3.5."
        "3.7...2.9"
        ".9.....8."),
    solution: SudokuBoard.fromString("987654123"
        "241973658"
        "653281974"
        "379846215"
        "524319786"
        "816527349"
        "768492531"
        "432165897"
        "195738462"),
    variation: SudokuVariation.diagonal,
    difficulty: 3.3,
  ),
  SudokuPuzzle(
    initialBoard: SudokuBoard.fromString(".6.....5."
        "8...5...6"
        "...6.1..."
        ".45...78."
        "........."
        ".27...14."
        "...9.8..."
        "2...3...1"
        ".9.....3."),
    solution: SudokuBoard.fromString("164372859"
        "872459316"
        "539681274"
        "945216783"
        "381547692"
        "627893145"
        "413968527"
        "258734961"
        "796125438"),
    variation: SudokuVariation.diagonal,
    difficulty: 5.0,
  ),
];
