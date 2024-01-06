(defun get-file-content (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

(defvar lines (get-file-content "tinp"))

;; (loop for i = 0 then (+ i 1)
;;       collect (print (length (nth i lines)))
;;       while (< i 1))

(defun split (line)
  (let ((left 0)
        (right 0))
    (loop
     (= left right)
     (+ right 2)
     collect (subseq line left right)
     while (< right (length line)))))

(loop for line in lines
      collect (print (split line)))

;; (loop for i = 0 then (+ i 1)
;;       collect (print i)
;;       while (< i 4))

;; (print l)
