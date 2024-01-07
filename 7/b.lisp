;;; common lisp

(defun get-file-content (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

(defun hidden-split (a ch)
  (let ((space-pos (position ch a)))
    (if (not space-pos)
        (list a)
        (nconc (list (subseq a 0 space-pos)) (hidden-split (subseq a (+ space-pos 1)) ch)))))

(defun split (a ch)
  (remove-if
   (lambda (x) (equal x ""))
   (hidden-split a ch)))

(defun add-card-value (counts i amount)
  (nconc
   (nconc
    (subseq counts 0 i)
    (list (list
           (nth 0 (nth i counts))
           (+ (nth 1 (nth i counts)) amount))))
   (subseq counts (+ i 1))))

(defun count-cards* (hand counts)
  (if (= (length hand) 0)
      counts
      (let ((ch (char hand 0))
            (hand-tail (subseq hand 1)))
        (let ((pos (position-if (lambda (count) (equal (car count) ch)) counts))
              (add-amount (if (equal ch #\J) 0 1)))
          (if (null pos)
              (count-cards* hand-tail (nconc counts (list (list ch add-amount))))
              (count-cards* hand-tail (add-card-value counts pos add-amount)))))))

(defun count-cards (hand)
  (sort
   (count-cards* hand (list))
   (lambda (x y) (> x y))
   :key (lambda (x) (nth 1 x))))

(defun count-jockers (hand)
  (reduce
   #'+
   (mapcar
    (lambda (x) (if (equal x #\J) 1 0))
    (loop for i from 0 to (- (length hand) 1) collect (char hand i)))))

(defun type-score (hand)
  (let ((counts (mapcar (lambda (x) (nth 1 x)) (count-cards hand)))
        (jockers (count-jockers hand)))
    (let ((first (+ (car counts) jockers)))
      (if (= first 5)
          9
          (if (= first 4)
              8
              (if (and (= first 3) (= (nth 1 counts) 2))
                  6
                  (if (= first 3)
                      5
                      (if (and (= first 2) (= (nth 1 counts) 2))
                          3
                          (if (= first 2)
                              1
                              0)))))))))

(defun card-score (ch)
  (cond ((equal ch #\J) 1)
        ((equal ch #\2) 2)
        ((equal ch #\3) 3)
        ((equal ch #\4) 4)
        ((equal ch #\5) 5)
        ((equal ch #\6) 6)
        ((equal ch #\7) 7)
        ((equal ch #\8) 8)
        ((equal ch #\9) 9)
        ((equal ch #\T) 10)
        ((equal ch #\Q) 12)
        ((equal ch #\K) 13)
        ((equal ch #\A) 14)))

(defun score-for-positions (hand)
  (if (= (length hand) 0)
      0
      (+ (* (card-score (char hand 0)) (expt 16 (+ (length hand) 1))) (score-for-positions (subseq hand 1)))))

(defun score (hand)
  (+ (* (type-score hand) 1000000000000) (score-for-positions hand)))



(defvar lines (get-file-content "inp"))
(defvar hands (mapcar (lambda (x) (split x #\SPACE)) lines))

(defvar sorted-hands (stable-sort hands
                           (lambda (x y) (< (score x) (score y)))
                           :key (lambda (x) (nth 0 x))))

(defvar winings (loop for i from 0 and x in sorted-hands
                      collect (* (+ i 1) (parse-integer (nth 1 x)))))

(print sorted-hands)
(print (reduce #'+ winings))
