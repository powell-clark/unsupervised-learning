# STORY-UL29: Lockstep README and Status-Line Shape Across the Four ML Repos

As a maintainer I want the four ML curriculum repos (supervised-learning, unsupervised-learning,
reinforcement-learning, deep-learning) to share one README shape and one status-line format so
that the portfolio reads as one coherent body of work rather than four independently-evolved
repos. The kernel measured they do not share one today (per MSG-EGLPK004: this repo's status
line predated this session's update, and the other three each phrase completion differently).

## Recommendation (per MSG-EGLPK006 item 3: "do the recommended")

This repo cannot edit another repo's README directly. The recommended path:
1. Propose this repo's own README shape (rebuilt this session: "The series" cross-link block,
   a per-part "Completed Lessons" section with one line per notebook, a single **Status:**
   line reading "N of N lessons complete (M notebooks)", Technical Stack, Learning Path,
   Related Repositories) as the CANONICAL candidate — it is the most recently rebuilt and
   already follows a clean, consistent structure.
2. Publish that candidate to EGLPK for a ruling across all four repos, since aligning
   sibling repos' READMEs is a cross-repo call the cockpit owns (federation-router.md:
   "Route here: anything that spans repos"), not something one repo's session does
   unilaterally to another repo's files.
3. Once a canonical shape is ruled on, audit and align THIS repo's own README against it
   (likely already close to compliant, since it is the proposed candidate) — that part is
   this repo's own, biddable work.
4. Aligning the other three repos' READMEs is explicitly out of scope for a session working
   in this repo; it is tracked at the kernel level or dispatched to each repo's own session.

## Acceptance Criteria

- [ ] Canonical README shape proposed to EGLPK (this repo's own shape, as above)
- [ ] Ruling received and this repo's README audited against it, gaps fixed if any
- [ ] No attempt made to edit supervised-learning, reinforcement-learning, or deep-learning's
      README files directly from this repo's session

## Linked Entities

- Directive: DIRECT-UL26 (Maintain the curriculum as a living Feynman-style corpus)
- Tasks: none filed yet — filed once EGLPK rules on the canonical shape
