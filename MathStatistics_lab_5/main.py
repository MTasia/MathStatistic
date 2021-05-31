from norm_sample_2d import norm_sample_2d
import coeffs
from plot_drawer import draw_ellipse

_sizes = [20, 60, 100]
_cor_coefficients = [0, 0.5, 0.9]


def main(sizes: list, cor_coefficients, mixed: bool = False):
    for size in sizes:
        print("size =", size)
        for rho in cor_coefficients:

            ps = list()
            sps = list()
            qs = list()

            ps_sqr = list()
            sps_sqr = list()
            qs_sqr = list()

            for i in range(1000):
                tmp_sample = list()
                if not mixed:
                    tmp_sample = norm_sample_2d(0, 0, 1, 1, rho, size).get_data()
                else:
                    tmp_sample_1 = norm_sample_2d(0, 0, 1, 1, 0.9, size).get_data()
                    tmp_sample_2 = norm_sample_2d(0, 0, 10, 10, -0.9, size).get_data()
                    tmp_sample.append([0.9 * x1 + 0.1 * x2 for x1, x2 in zip(tmp_sample_1[0], tmp_sample_2[0])])
                    tmp_sample.append([0.9 * y1 + 0.1 * y2 for y1, y2 in zip(tmp_sample_1[1], tmp_sample_2[1])])

                ps.append(coeffs.pearson(tmp_sample))
                sps.append(coeffs.spearman(tmp_sample))
                qs.append(coeffs.quadrant(tmp_sample))

                ps_sqr.append(ps[-1] ** 2)
                sps_sqr.append(sps[-1] ** 2)
                qs_sqr.append(qs[-1] ** 2)

            p_mean = 0
            s_mean = 0
            q_mean = 0

            p_sqr_mean = 0
            s_sqr_mean = 0
            q_sqr_mean = 0

            for p, s, q, p_sqr, s_sqr, q_sqr in zip(ps, sps, qs, ps_sqr, sps_sqr, qs_sqr):
                p_mean += p
                s_mean += s
                q_mean += q
                p_sqr_mean += p_sqr
                s_sqr_mean += s_sqr
                q_sqr_mean += q_sqr

            p_mean /= 1000
            s_mean /= 1000
            q_mean /= 1000

            p_sqr_mean /= 1000
            s_sqr_mean /= 1000
            q_sqr_mean /= 1000

            print("$\\rho$ =", rho, "& $r_P$ & $r_S$ & $r_Q$ \\\\ \\hline")
            print("$E(z)$ &", '%.3f' % p_mean, "&", '%.3f' % s_mean, "&", '%.3f' % q_mean, "\\\\ \\hline")
            print("$E(z^2)$ &", '%.3f' % p_sqr_mean, "&", '%.3f' % s_sqr_mean, "&", '%.3f' % q_sqr_mean, "\\\\ \\hline")
            print("$D(z)$ &", '%.3f' % abs(p_mean ** 2 - p_sqr_mean), "&", '%.3f' % abs(s_mean ** 2 - s_sqr_mean), "&",
                  '%.3f' % abs(q_mean ** 2 - q_sqr_mean),
                  "\\\\ \\hline")
            draw_ellipse(norm_sample_2d(0, 0, 1, 1, rho, size), mixed)


main(_sizes, _cor_coefficients)
# main(_sizes, [0], mixed=True)
