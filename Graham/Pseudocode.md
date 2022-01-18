    GRAHAM_SCAN(L):

    Step1:  If Len(L) < 3 then
                Set S = Stack()
                S.PUSH(L[0])
                S.PUSH(L[1])
                S.PUSH(L[2])
                Goto Step 3
            Else:
                Set P0 = MIN(L, key = y)
                REMOVE_VAL(L, P0)
                SORT_BY_POLAR(L, P0)

                Set S = Stack()
                S.PUSH(P0)
                S.PUSH(L[0])
                S.PUSH(L[1])
            EndIf

    Step2:  Repeat For I = 2 to Len(L) do
                Set P1 = S.NEXT_TO_TOP()
                Set P2 = S.TOP()
                Set P3 = L[i]

                Set A = P2 - P1
                Set B = P3 - P1

                Repeat S.SIZE() > 2 and While A.Cross(B).z < 0 do
                    S.POP()
                Done

                S.PUSH(P3)
            End

    Step3: Print "Points in Convex Hull are S"

    Step4: Exit